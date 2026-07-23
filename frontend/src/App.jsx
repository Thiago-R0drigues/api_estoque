import { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [produtos, setProdutos] = useState([]);
  const [nome, setNome] = useState("");
  const [quantidade, setQuantidade] = useState("");
  const [editandoId, setEditandoId] = useState(null);

  const URL_API = 'https://api-estoque-rcyp.onrender.com'

  const buscarProdutos = () => {
    fetch(`${URL_API}/produtos`)
      .then((res) => res.json())
      .then((data) => setProdutos(data))
      .catch((err) => console.error("Erro ao buscar produtos:", err));
  };

  useEffect(() => {
    buscarProdutos();
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();

    const url = editandoId
      ? `${URL_API}/produtos/${editandoId}`
      : `${URL_API}/produtos`;
    const method = editandoId ? "PUT" : "POST";

    fetch(url, {
      method,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ nome, quantidade: Number(quantidade) }),
    })
      .then((res) => res.json())
      .then(() => {
        setNome("");
        setQuantidade("");
        setEditandoId(null);
        buscarProdutos();
      })
      .catch((err) => console.error("Erro ao salvar produto:", err));
  };

  const handleEditar = (produto) => {
    setNome(produto.nome);
    setQuantidade(produto.quantidade);
    setEditandoId(produto.id);
  };

  const handleDeletar = (id) => {
    fetch(`${URL_API}/produtos/${id}`, { method: "DELETE" })
      .then(() => buscarProdutos())
      .catch((err) => console.error("Erro ao deletar produto:", err));
  };

  const handleCancelar = () => {
    setNome("");
    setQuantidade("");
    setEditandoId(null);
  };

  return (
    <div className="container">
      <h1>Estoque</h1>

      <form onSubmit={handleSubmit} className="form">
        <input
          type="text"
          placeholder="Nome do produto"
          value={nome}
          onChange={(e) => setNome(e.target.value)}
          required
        />
        <input
          type="number"
          placeholder="Quantidade"
          value={quantidade}
          onChange={(e) => setQuantidade(e.target.value)}
          required
        />
        <button type="submit">
          {editandoId ? "Salvar" : "Cadastrar"}
        </button>
        {editandoId && (
          <button type="button" onClick={handleCancelar} className="cancelar">
            Cancelar
          </button>
        )}
      </form>

      <ul className="lista">
        {produtos.map((p) => (
          <li key={p.id} className="item">
            <span>{p.nome} — {p.quantidade} unidades</span>
            <div className="acoes">
              <button onClick={() => handleEditar(p)}>Editar</button>
              <button onClick={() => handleDeletar(p.id)} className="deletar">
                Excluir
              </button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;